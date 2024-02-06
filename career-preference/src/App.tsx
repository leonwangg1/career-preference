import type { ReactElement } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { lazy, Suspense } from "react";
import { Survey } from "./pages/Survey";
import "./App.css";

const Welcome = lazy(async () => import("./pages/Welcome"));

export default function App(): ReactElement {
  return (
    <BrowserRouter>
      <Suspense fallback={<Loading />}>
        <Routes>
          <Route path="/" element={<Welcome />} />
          <Route path="/survey" element={<Survey />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}

function Loading() {
  return <h2>Loading...</h2>;
}
