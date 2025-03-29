import React from "react";

interface TextBoxProps extends React.InputHTMLAttributes<HTMLInputElement> {
    label?: string;
}

const TextBox: React.FC<TextBoxProps> = ({ label, ...props }) => {
    return (
        <div className="w-full max-w-md">
            {label && (
                <label className="block mb-2 text-sm font-medium text-gray-900">
                    {label}
                </label>
            )}
            <input
                type="text"
                className="block w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
                {...props}
            />
        </div>
    );
};

export default TextBox;
