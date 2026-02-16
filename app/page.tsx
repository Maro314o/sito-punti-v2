import ButtonsWrapper from "@/components/modules/ButtonsWrapper/page";
import FormWrapper from "@/components/modules/FormWrapper/page";
import Navbar from "@/components/modules/Navbar/page";
import TitleWrapper from "@/components/modules/TitleWrapper/page";

export default function Home() {
  return (
    <div>
      <Navbar />
      <TitleWrapper title={"One Piece"} />
      <FormWrapper />
      <ButtonsWrapper />
    </div>
  );
}
