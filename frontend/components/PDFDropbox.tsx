"use client";

import React, { useState, DragEvent, ChangeEvent } from "react";

const PDFDropbox: React.FC = () => {
    const [dragActive, setDragActive] = useState(false);
    const [fileName, setFileName] = useState<string | null>(null);

    const handleDrag = (e: DragEvent<HTMLLabelElement>) => {
        e.preventDefault();
        e.stopPropagation();
        if (e.type === "dragenter" || e.type === "dragover") {
            setDragActive(true);
        } else if (e.type === "dragleave") {
            setDragActive(false);
        }
    };

    const handleDrop = (e: DragEvent<HTMLLabelElement>) => {
        e.preventDefault();
        e.stopPropagation();
        setDragActive(false);
        if (e.dataTransfer.files && e.dataTransfer.files[0]) {
            const file = e.dataTransfer.files[0];
            if (file.type === "application/pdf") {
                setFileName(file.name);
            } else {
                alert("Please upload a PDF file.");
            }
        }
    };

    const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
        if (e.target.files && e.target.files[0]) {
            const file = e.target.files[0];
            if (file.type === "application/pdf") {
                setFileName(file.name);
            } else {
                alert("Please upload a PDF file.");
            }
        }
    };

    return (
        <div className="w-full max-w-md">
            <label
                htmlFor="pdf-upload"
                onDragEnter={handleDrag}
                onDragOver={handleDrag}
                onDragLeave={handleDrag}
                onDrop={handleDrop}
                className={`flex flex-col items-center justify-center w-full h-32 border-2 border-dashed rounded-lg cursor-pointer transition-colors ${dragActive ? "border-blue-400 bg-blue-50" : "border-gray-300"
                    }`}
            >
                <span className="text-gray-500">
                    {fileName || "Drag and drop a PDF here or click to select"}
                </span>
                <input
                    type="file"
                    id="pdf-upload"
                    accept="application/pdf"
                    onChange={handleChange}
                    className="hidden"
                />
            </label>
        </div>
    );
};

export default PDFDropbox;
