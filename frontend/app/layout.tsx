import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "LLM-Based Harness Generator",
  description:
    "Generate test harnesses for detecting memory leaks in code using LLMs",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <div className="app-container">{children}</div>
      </body>
    </html>
  );
}
