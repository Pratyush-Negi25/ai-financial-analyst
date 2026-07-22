import { useState } from "react";
import { uploadPDF } from "../services/api";

function Upload() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [status, setStatus] = useState("No file selected");

  const handleFileChange = (event) => {
    const file = event.target.files[0];

    setSelectedFile(file);

    if (file) {
      setStatus(file.name);
    } else {
      setStatus("No file selected");
    }
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please select a PDF first.");
      return;
    }

    try {
      setStatus("Uploading...");

      const result = await uploadPDF(selectedFile);

      setStatus(
        `Uploaded successfully! ${result.chunks} chunks created.`
      );

      console.log(result);
    } catch (error) {
      console.error(error);
      setStatus("Upload failed.");
    }
  };

  return (
    <section className="card">
      <h2>Upload Financial Report</h2>

      <p>Select a PDF financial report.</p>

      <br />

      <input
        type="file"
        accept=".pdf"
        onChange={handleFileChange}
      />

      <br />
      <br />

      <button onClick={handleUpload}>
        Upload PDF
      </button>

      <br />
      <br />

      <strong>Status:</strong> {status}
    </section>
  );
}

export default Upload;