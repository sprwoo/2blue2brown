"use client";

import { Button } from "@/components/ui/button";
import PDFDropbox from "@/components/PDFDropbox";
import TextBox from "@/components/TextBox";
import { useEffect, useState } from "react";

export default function Home() {
  useEffect(() => {
    const fetchBroskis = async () => {
      try {
        const response = await fetch("http://127.0.0.1:5001/api");
        const result = await response.json();
        console.log("result", result);
      } catch (error) {
        console.error(error);
      }
    };
    fetchBroskis();
  }, []);
  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-8 gap-8">
      <h1 className="text-3xl font-bold">PDF Upload & Text Input</h1>
      <PDFDropbox />
      <TextBox placeholder="Enter your text here..." />
      <Button className="bg-red-100">Submit</Button>
    </div>
  );
}
