import FormWrapper from "@/components/modules/FormWrapper/page";
import InfoProfile from "@/components/modules/InfoProfile/page";
import TitleWrapper from "@/components/modules/TitleWrapper/page";

export default function profilo() {
  return (
    <div className="pt-30">
      <TitleWrapper title={"Profilo"} />
      <FormWrapper p="logged" />
      <InfoProfile />
    </div>
  );
}
