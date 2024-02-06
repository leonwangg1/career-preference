import { Link } from "react-router-dom";
import { TriangleIcon } from "../components/Icon";

export default function Welcome() {
  return (
    <div className="flex flex-col items-center justify-center text-[#070b0e]">
      <div className="bg-[#e8edef] p-6 rounded-lg shadow-xl w-full">
        <div className="flex flex-col items-center justify-between border-b border-gray-300 pb-4">
          <TriangleIcon className="text-[#4bb5f7] text-3xl mb-2" />
          <h1 className="text-xl font-semibold text-center flex-1 ml-4">
            Land Engineering Agency Career Preference Tool
          </h1>
        </div>
        <div className="container-body px-2 text-pretty">
          <div className="mt-6 text-left">
            <h1 className="text-l font-semibold">Privacy Statement</h1>
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
            <h1 className="text-l font-semibold">
              What information will be collected?
            </h1>
            <p className="mt-3 text-sm">
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
            <Link to={`/survey`} className="text-white">
              <button className="btnNav">Accept & Proceed</button>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
