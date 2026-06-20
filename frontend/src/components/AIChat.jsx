import { useState } from "react";
import axios from "axios";


function AIChat({ city }) {

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const askAI = async () => {

    if (!question.trim()) {
      alert("Enter a question");
      return;
    }

    try {

      setLoading(true);
      setAnswer("");

      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          city: city,
          question: question
        }
      );

      setAnswer(
        response.data.answer
      );

    } catch (error) {

      console.error(error);

      setAnswer(
        "Failed to get AI response."
      );

    } finally {

      setLoading(false);

    }
  };

  return (

    <div className="card">

      <h2>
        🤖 GreenShield AI Assistant
      </h2>

      <p>
        Ask sustainability questions
        about <strong>{city}</strong>
      </p>

      <textarea
        rows="4"
        placeholder="Example: Why is Agra's heat risk high?"
        value={question}
        onChange={(e) =>
          setQuestion(e.target.value)
        }
        style={{
          width: "100%",
          padding: "10px",
          borderRadius: "8px",
          marginBottom: "10px"
        }}
      />

      <button
        className="analysis-btn"
        onClick={askAI}
        disabled={loading}
      >
        {loading
          ? "Thinking..."
          : "Ask AI"}
      </button>

      {answer && (

        <div
          style={{
            marginTop: "20px",
            padding: "15px",
            background: "#f5f5f5",
            borderRadius: "10px",
            whiteSpace: "pre-wrap"
          }}
        >

          <h3>
            🤖 AI Response
          </h3>

          <div
          style={{
          whiteSpace: "pre-wrap",
          lineHeight: "1.8",
          fontSize: "16px"
          }}
           >
        {answer}
        </div>
        </div>

      )}

    </div>

  );
}

export default AIChat;