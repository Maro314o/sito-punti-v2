import FormWrapper from "@/components/modules/FormWrapper/page";
import Image from "next/image";

export default function Home() {
  return (
    <div>
      <TitleWrapper title={"a"} subtitle={"b"} />
      <FormWrapper />
    </div>
  );
}

const TitleWrapper = ({
  title,
  subtitle,
  imageUrl,
}: {
  title: string;
  subtitle: string;
  imageUrl?: string;
}) => {
  return (
    <div className="container">
      <h1>{title}</h1>
      <h2>{subtitle}</h2>
      <Image src={imageUrl || ""} alt={""} />
    </div>
  );
};
