import { Geist, Geist_Mono } from "next/font/google"

import "./globals.css"
import { Providers } from "@/providers"
import { cn } from "@/lib/utils"

const fontSans = Geist({
  subsets: ["latin"],
  variable: "--font-sans",
})

const fontMono = Geist_Mono({
  subsets: ["latin"],
  variable: "--font-mono",
})

export const metadata = {
  title: "Epidemia",
  description: "Sistema de monitoramento epidemiológico",
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html
      lang="pt-BR"
      suppressHydrationWarning
      className={cn("antialiased", fontMono.variable, "font-sans", fontSans.variable)}
    >
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  )
}
