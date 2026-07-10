const welcome = document.getElementById("welcome");
const chatBox = document.getElementById("chat-box");
const input = document.getElementById("question");

function addUserMessage(message) {
  chatBox.innerHTML += `
        <div class="flex justify-end">
            <div class="bg-blue-600 max-w-2xl px-5 py-4 rounded-2xl rounded-br-sm shadow">
                ${message}
            </div>
        </div>
    `;

  chatBox.scrollTop = chatBox.scrollHeight;
}

async function addBotMessage(message, pages) {

  const pagesHTML = pages.length
    ? pages.map(p => `
            <span class="px-3 py-1 bg-slate-700 rounded-full text-sm">
                📄 Page ${p}
            </span>
        `).join("")
    : "";

  const id = "msg_" + Date.now();

  chatBox.innerHTML += `
        <div class="flex">

            <div class="bg-slate-800 max-w-3xl px-5 py-4 rounded-2xl rounded-bl-sm shadow">

                <div id="${id}" class="prose prose-invert max-w-none"></div>

                <div class="mt-5 flex flex-wrap gap-2">

                    ${pagesHTML}

                </div>

            </div>

        </div>
    `;

  chatBox.scrollTop = chatBox.scrollHeight;

  const target = document.getElementById(id);

  const html = marked.parse(message);

  let current = "";

  for (let i = 0; i < html.length; i++) {

    current += html[i];

    target.innerHTML = current;

    chatBox.scrollTop = chatBox.scrollHeight;

    await new Promise(r => setTimeout(r, 4));

  }

}

function showLoading() {

  chatBox.innerHTML += `
        <div id="loading" class="flex">

            <div class="bg-slate-800 px-5 py-4 rounded-2xl">

                🤖 Thinking...

            </div>

        </div>
    `;

  chatBox.scrollTop = chatBox.scrollHeight;
}

function removeLoading() {

  const loading = document.getElementById("loading");

  if (loading) {

    loading.remove();

  }

}

async function sendQuestion() {

  const question = input.value.trim();

  if (!question) return;

  if (welcome) {
    welcome.remove();
  }

  addUserMessage(question);

  input.value = "";

  showLoading();

  try {

    const response = await fetch("/chat", {

      method: "POST",

      headers: {
        "Content-Type": "application/json"
      },

      body: JSON.stringify({
        question: question
      })

    });

    const data = await response.json();

    removeLoading();

    await addBotMessage(
      data.answer,
      data.pages
    );

  }

  catch (err) {

    removeLoading();

    await addBotMessage(
      "❌ Something went wrong.",
      []
    );
  }

}

function newChat() {

  chatBox.innerHTML = "";

}

input.addEventListener("keydown", function (e) {

  if (e.key === "Enter" && !e.shiftKey) {

    e.preventDefault();

    sendQuestion();

  }

});