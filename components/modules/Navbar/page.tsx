"use client";

import * as React from "react";
import Link from "next/link";
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  navigationMenuTriggerStyle,
} from "@/components/ui/navigation-menu";

export default function Navbar() {
  return (
    <div className="pt-10 fixed w-full">
      <NavigationMenu className="border bg-background shadow-xs whitespace-nowrap rounded-md">
        <div className="flex md:hidden">
          <MobileContent />
        </div>
        <div className="hidden md:flex">
          <DesktopContent />
        </div>
      </NavigationMenu>
    </div>
  );
}

function ListItem({
  title,
  href,
  ...props
}: React.ComponentPropsWithoutRef<"li"> & { href: string }) {
  return (
    <li {...props}>
      <NavigationMenuLink asChild>
        <Link href={href}>
          <div className="flex flex-col gap-1 text-sm">
            <div className="leading-none font-medium">{title}</div>
          </div>
        </Link>
      </NavigationMenuLink>
    </li>
  );
}

const MobileContent = () => {
  return (
    <NavigationMenuList>
      <NavigationMenuItem>
        <NavigationMenuLink asChild className={navigationMenuTriggerStyle()}>
          <Link href="/">Home</Link>
        </NavigationMenuLink>
      </NavigationMenuItem>
      <NavigationMenuItem>
        <NavigationMenuLink asChild className={navigationMenuTriggerStyle()}>
          <Link href="/profilo">Profilo</Link>
        </NavigationMenuLink>
      </NavigationMenuItem>
      <NavigationMenuItem>
        <NavigationMenuTrigger>Informazioni</NavigationMenuTrigger>
        <NavigationMenuContent>
          <ul className="w-66">
            <ListItem href="/" title="Caccia al tesoro"></ListItem>
            <ListItem href="/" title="Rotte"></ListItem>
            <ListItem href="/" title="Misteri"></ListItem>
            <ListItem href="/" title="Regole"></ListItem>
          </ul>
        </NavigationMenuContent>
      </NavigationMenuItem>
    </NavigationMenuList>
  );
};

const DesktopContent = () => {
  return (
    <NavigationMenuList>
      <NavigationMenuItem>
        <NavigationMenuLink asChild className={navigationMenuTriggerStyle()}>
          <Link href="/">Home</Link>
        </NavigationMenuLink>
      </NavigationMenuItem>
      <NavigationMenuItem>
        <NavigationMenuLink asChild className={navigationMenuTriggerStyle()}>
          <Link href="/profilo">Profilo</Link>
        </NavigationMenuLink>
      </NavigationMenuItem>
      <NavigationMenuItem>
        <NavigationMenuLink asChild className={navigationMenuTriggerStyle()}>
          <Link href="/">Caccia al tesoro</Link>
        </NavigationMenuLink>
      </NavigationMenuItem>
      <NavigationMenuItem>
        <NavigationMenuLink asChild className={navigationMenuTriggerStyle()}>
          <Link href="/">Rotte</Link>
        </NavigationMenuLink>
      </NavigationMenuItem>
      <NavigationMenuItem>
        <NavigationMenuLink asChild className={navigationMenuTriggerStyle()}>
          <Link href="/">Misteri</Link>
        </NavigationMenuLink>
      </NavigationMenuItem>
      <NavigationMenuItem>
        <NavigationMenuLink asChild className={navigationMenuTriggerStyle()}>
          <Link href="/">Regole</Link>
        </NavigationMenuLink>
      </NavigationMenuItem>
    </NavigationMenuList>
  );
};
