import { useState } from "react";

function App() {
  const [script, setScript] = useState("");
  const [status, setStatus] = useState("");

  const generateVideo = async () => {
    setStatus("Processing...");
    const res = await fetch("/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ script }),
    });
    const data = await res.json();
    setStatus("Done! File: " + data.file);
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">AI Movie Creator 🎬</h1>
      <textarea
        className="border w-full p-2 mt-4"
        rows="6"
        placeholder="Enter your movie script..."
        value={script}
        onChange={(e) => setScript(e.target.value)}
      />
      <button
        className="mt-4 bg-blue-500 text-white px-4 py-2 rounded"
        onClick={generateVideo}
      >
        Generate Movie
      </button>
      <p className="mt-4">{status}</p>
    </div>
  );
}

export default App;
