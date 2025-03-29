"use client";

import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Plus } from "lucide-react";

const mockChats = [
  { id: 1, title: "Math Notes", timestamp: "Mar 28" },
  { id: 2, title: "Physics PDF", timestamp: "Mar 27" },
  { id: 3, title: "AI Chat", timestamp: "Mar 25" },
];

export default function Sidebar() {
  return (
    <div className="w-64 bg-zinc-900 border-r border-zinc-700 flex flex-col">
      <div className="p-4 border-b border-zinc-700">
        <Button className="w-full" variant="secondary">
          <Plus className="mr-2 h-4 w-4" />
          New Chat
        </Button>
      </div>
      <ScrollArea className="flex-1">
        <div className="p-4 space-y-2">
          {mockChats.map((chat) => (
            <div
              key={chat.id}
              className="p-3 rounded-lg bg-zinc-800 hover:bg-zinc-700 cursor-pointer"
            >
              <div className="text-sm font-medium">{chat.title}</div>
              <div className="text-xs text-zinc-400">{chat.timestamp}</div>
            </div>
          ))}
        </div>
      </ScrollArea>
    </div>
  );
}
