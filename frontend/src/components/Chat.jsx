import { useState } from "react";
import { askQuestion } from "../services/api";

function Chat() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("Upload a report and ask a question.");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!question.trim()) {
      alert("Please enter a question.");
      return;
    }

    try {
      setLoading(true);

      const result = await askQuestion(question);

      setAnswer(result.answer);

      setQuestion("");
    } catch (error) {
      console.error(error);
      setAnswer("Failed to get AI response.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="card">
      <h2>Chat with Financial Report</h2>

      <p>Ask questions about the uploaded financial report.</p>

      <br />

      <textarea
        rows="4"
        placeholder="Ask a question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <br />
      <br />

      <button onClick={handleSend} disabled={loading}>
        {loading ? "Thinking..." : "Send"}
      </button>

      <br />
      <br />

      <strong>AI Response:</strong>

      <p>{answer}</p>
    </section>
  );
}

export default Chat;