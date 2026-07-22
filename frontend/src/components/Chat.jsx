import { useState } from "react";
import { askQuestion } from "../services/api";

function Chat() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState(
    "Upload a financial report and ask your first question."
  );
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
      setAnswer("❌ Failed to get AI response.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="card">
      <h2>Chat with Financial Report</h2>

      <p>
        Ask AI questions about the uploaded annual report using
        Retrieval-Augmented Generation (RAG).
      </p>

      <textarea
        rows="5"
        placeholder="Example: What was Amazon's total revenue in 2024?"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button onClick={handleSend} disabled={loading}>
        {loading ? "Thinking..." : "Send Question"}
      </button>

      <h3>AI Response</h3>

      <div className="response-card">
        {answer}
      </div>
    </section>
  );
}

export default Chat;