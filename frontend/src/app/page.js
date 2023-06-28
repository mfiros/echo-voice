import Image from "next/image";
import Main from "./components/main";
export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-2">
      <Main />
    </div>
  );
}
