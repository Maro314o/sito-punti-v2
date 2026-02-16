import FormWrapper from "@/components/modules/FormWrapper/page";
import TitleWrapper from "@/components/modules/TitleWrapper/page";

const profilo = () => {
  return (
    <div className="pt-30">
      <TitleWrapper title={"Profilo"} />
      <FormWrapper p="logged" />
    </div>
  );
};

export default profilo;
