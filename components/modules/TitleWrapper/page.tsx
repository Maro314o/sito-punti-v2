import Image from "next/image";

export default function TitleWrapper() {
  const title = "ISIS Keynes";
  const imageUrl = "";
  return (
    <div className="container mx-auto text-center w-auto md:w-xl lg:w-4xl">
      <Image src={imageUrl || ""} alt={""} />
      <h1 className="text-3xl md:text-5xl lg:text-6xl">{title}</h1>
    </div>
  );
}
