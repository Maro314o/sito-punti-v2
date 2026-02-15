import FormWrapper from "@/components/modules/FormWrapper/page";
import TitleWrapper from "@/components/modules/TitleWrapper/page";

export default function Home() {
  return (
    <div className="p-10 md:p-20 lg:p-30">
      <TitleWrapper />
      <FormWrapper />
    </div>
  );
}
