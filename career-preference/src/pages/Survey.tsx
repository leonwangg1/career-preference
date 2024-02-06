import { useState } from "react";
import { Link } from "react-router-dom";

export function Survey() {
  // Assuming you have a setup to interact with your database
  // For demonstration, using useState instead of useDocument
  const [preferences, setPreferences] = useState({
    name: "",
    currentEmploymentCategory: "",
    skillsAndExperiences: [],
    interests: [],
    careerProgression: "",
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Preferences submitted: ", preferences);
    // Here you would use useLiveQuery.database.put to submit to your database
  };

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setPreferences((prev) => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  return (
    <div className="flex flex-col items-center justify-center text-[#070b0e]">
      <div className="bg-[#e8edef] p-6 rounded-lg shadow-xl w-full">
        <div className="flex flex-col items-center justify-between border-b border-gray-300 pb-4">
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
            <form
              onSubmit={handleSubmit}
              className="space-y-4 max-w-xl mx-auto my-10"
            >
              <div>
                <label
                  htmlFor="name"
                  className="block text-sm font-medium text-gray-700"
                >
                  Name
                </label>
                <input
                  type="text"
                  name="name"
                  id="name"
                  onChange={handleChange}
                  className="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2"
                />
              </div>
              <div className="btn-container">
                <button className="btn">
                  <Link to={`/`} className="text-white">
                    Previous
                  </Link>
                </button>
                <button type="submit" className="btn">
                  Submit
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}
