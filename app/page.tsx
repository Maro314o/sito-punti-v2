import ButtonsWrapper from "@/components/modules/ButtonsWrapper/page";
import FormWrapper from "@/components/modules/FormWrapper/page";
import TitleWrapper from "@/components/modules/TitleWrapper/page";

export default function Home() {
  return (
    <div className="pt-30">
      <TitleWrapper title={"One Piece"} />
      <FormWrapper />
      <ButtonsWrapper />
    </div>
  );
}
