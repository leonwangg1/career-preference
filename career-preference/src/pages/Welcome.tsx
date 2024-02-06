import { SVGProps } from "react";
import { JSX } from "react/jsx-runtime";
import { Link } from "react-router-dom";

export default function Welcome() {
  return (
    <div className="flex flex-col items-center justify-center text-[#070b0e]">
      <div className="bg-[#e8edef] p-6 rounded-lg shadow-xl w-full">
        <div className="flex flex-col items-center justify-between border-b border-gray-300 pb-4">
          <TriangleIcon className="text-[#4bb5f7] text-3xl mb-2" />
          <h1 className="text-lg font-semibold text-center flex-1 ml-4">
            Land Engineering Agency Career Preference Tool
          </h1>
        </div>
        <div className="container-body px-2 text-pretty">
          <div className="mt-6 text-left">
            <h1 className="text-xl md:text-2xl font-semibold">
              Privacy Statement
            </h1>
            <p className="mt-3 text-sm">
              All data collected as part of LEA Career Preference Tool will be
              securely stored in the CIOG Central Data Centre in Fyshwick ACT.
              Your raw data will only be accessed by the Data Manager
              responsible for this Tool and LEA WFP Cell for the purposes of
              understanding your career preferences and where appropriate
              matching you against vacant roles. If matched against a vacant
              role within the Land Engineering Agency, we may discuss your
              appropriateness for the role with yourself, the vacant role
              delegate and/or with your Chain of Command.
            </p>
          </div>
          <div className="mt-3 text-left">
            <h1 className="text-xl md:text-2xl font-semibold">
              What information will be collected?
            </h1>
            <p className="mt-3 text-sm ">
              The purpose of Land Engineering Agency Career Preference tool is
              to gain an understanding of your current skills, knowledge and
              experience and your future career preferences Participation is
              encouraged however voluntary. Management permission is not
              required to participate in this exercise however when considering
              your suitability for an opportunity, your Chain of Command may be
              consulted.
            </p>
            <p className="mt-3 text-sm">
              Your information will be used to understand your career
              preferences, provide you with new opportunities where requested
              and appropriate, and to support you in having a meaningful career
              within LEA. Please take the time to fill out the attached document
              honestly and with as much detail as possible. If your preferences
              change at any time, we encourage you to resubmit this form.
            </p>
          </div>
          <div className="mt-6 flex justify-center">
            <button className="btn">
              <Link to={`/survey`} className="text-white">
                Accept & Proceed
              </Link>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

function TriangleIcon(
  props: JSX.IntrinsicAttributes & SVGProps<SVGSVGElement>
) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="60"
      height="60"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z" />
    </svg>
  );
}
