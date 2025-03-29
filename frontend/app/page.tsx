"use client";

import { Button } from "@/components/ui/button";
import PDFDropbox from "@/components/PDFDropbox";
import TextBox from "@/components/TextBox";
import { useEffect, useState } from "react";

export default function Home() {
  const [message, setMessage] = useState("");
  const [responseMessage, setResponseMessage] = useState("");

  useEffect(() => {
    const fetchBroskis = async () => {
      try {
        const response = await fetch(
          "http://127.0.0.1:5001/api/check_connection"
        );
        const result = await response.json();
        console.log("GET request result:", result);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    fetchBroskis();
  }, []);

  const handlePostRequest = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5001/api/post_test", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          sender: "user",
          message: message,
        }),
      });

      const result = await response.json();
      console.log("POST request result:", result);
      setResponseMessage(
        result.success ? "Message posted successfully!" : result.error
      );
    } catch (error) {
      console.error("Error posting data:", error);
      setResponseMessage("Error posting data.");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-8 gap-8">
      <h1 className="text-3xl font-bold">PDF Upload & Text Input</h1>
      <PDFDropbox />
      <TextBox
        placeholder="Enter your text here..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <Button className="bg-red-100" onClick={handlePostRequest}>
        Submit
      </Button>
      {responseMessage && <p>{responseMessage}</p>}
    </div>
  );
}
