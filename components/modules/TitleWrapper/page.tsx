import CldImage from "@/components/ui/CldImage";
export default function TitleWrapper({ title }: { title: string }) {
  return (
    <div className="text-center grid grid-col gap-5 md:gap-10 lg:gap-15">
      <CldImage
        src="logo_brjkfy"
        alt=""
        width={100}
        height={100}
        className="mx-auto"
      />
      <h2 className="text-1xl md:text-3xl lg:text-4xl">ISIS Keynes</h2>
      <h1 className="text-3xl md:text-5xl lg:text-6xl">{title}</h1>
    </div>
  );
}
