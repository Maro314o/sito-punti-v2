import { Button } from "@/components/ui/button";
import Image from "next/image";
import location from "@/public/icons/location.svg";
import mail from "@/public/icons/mail.svg";
import github from "@/public/icons/github.svg";

export default function ButtonsWrapper() {
  return (
    <div className="flex flex-row gap-5 mx-auto w-min">
      <div>
        <Button variant={"link"} size={"icon"}>
          <Image src={location} alt={""} width={40} height={40} />
        </Button>
      </div>
      <div>
        <Button variant={"link"} size={"icon"}>
          <Image src={mail} alt={""} width={40} height={40} />
        </Button>
      </div>
      <div>
        <Button variant={"link"} size={"icon"}>
          <Image src={github} alt={""} width={40} height={40} />
        </Button>
      </div>
    </div>
  );
}
