import Image from "next/image";
import logo from "@/public/logo.png";
export default function TitleWrapper({ title }: { title: string }) {
  return (
    <div className="text-center pt-30 grid grid-col gap-5 md:gap-10 lg:gap-15">
      <Image src={logo} alt={""} width={100} height={100} className="mx-auto" />
      <h2 className="text-1xl md:text-3xl lg:text-4xl">ISIS Keynes</h2>
      <h1 className="text-3xl md:text-5xl lg:text-6xl">{title}</h1>
    </div>
  );
}
