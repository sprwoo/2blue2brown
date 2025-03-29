import { Button } from "@/components/ui/button";
import PDFDropbox from "@/components/PDFDropbox";
import TextBox from "@/components/TextBox";

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-8 gap-8">
      <h1 className="text-3xl font-bold">PDF Upload & Text Input</h1>
      <PDFDropbox />
      <TextBox placeholder="Enter your text here..." />
      <Button className="bg-red-100">Submit</Button>
    </div>
  );
}
