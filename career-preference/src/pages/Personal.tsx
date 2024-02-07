import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

import Select from "../components/Select";
import Input from "../components/Input";

import { TriangleIcon } from "../components/Icon";

export function Survey() {
  // States for question groups and questions
  const [questionGroups, setQuestionGroups] = useState([]);
  const [questions, setQuestions] = useState([]);

  // Fetch question groups on component mount
  useEffect(() => {
    fetch("http://127.0.0.1:5000/question_groups")
      .then((res) => {
        if (!res.ok) {
          throw new Error("Network response was not ok");
        }
        return res.json();
      })
      .then((data) => setQuestionGroups(data))
      .catch((error) =>
        console.error("There was a problem with your fetch operation:", error)
      );

    // Fetch all questions
    fetch("http://127.0.0.1:5000/questions")
      .then((res) => res.json())
      .then((data) => setQuestions(data))
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  return (
    <div className="flex flex-col items-center justify-center text-[#070b0e]">
      <div className="bg-[#e8edef] p-6 rounded-lg shadow-xl w-full">
        <div className="flex flex-col items-center justify-between border-b border-gray-300 pb-4">
          <TriangleIcon className="text-[#4bb5f7] text-3xl mb-2" />
          <h1 className="text-lg font-semibold text-center flex-1">
            Land Engineering Agency Career Preference Tool
          </h1>
        </div>
        <div className="container-body px-2 text-pretty">
          <div className="mt-3 text-left">
            <form
              // onSubmit={handleSubmit}
              className="space-y-4 max-w-xl mx-auto"
            >
              {questionGroups
                .filter(
                  (personalGroup) => personalGroup.TITLE === "Personal Details"
                )
                .map((filteredGroup) => (
                  <div key={filteredGroup.GROUP_ID}>
                    <h1 className="text-lg font-semibold">
                      {filteredGroup.TITLE}
                    </h1>
                    {questions
                      .filter(
                        (question) =>
                          question.GROUP_ID === filteredGroup.GROUP_ID
                      )
                      .map((filteredQuestion) => (
                        <div key={filteredQuestion.QUESTION_ID}>
                          <p className="mt-2">
                            {filteredQuestion.FIELD_LABEL}
                            {filteredQuestion.REQUIRED === 1 ? (
                              <span className="text-red-700">*</span>
                            ) : null}
                          </p>
                          {/* Render input based on FIELD_TYPE */}
                          {filteredQuestion.FIELD_TYPE === "freetext" ? (
                            <Input
                              placeholder={filteredQuestion.PLACEHOLDER}
                              limit={filteredQuestion.INPUT_LIMIT}
                            />
                          ) : (
                            filteredQuestion.FIELD_TYPE === "single_select" && (
                              <Select
                                placeholder={filteredQuestion.PLACEHOLDER}
                                values={filteredQuestion.POSSIBLE_VALUES.split(
                                  ";"
                                )}
                              />
                            )
                          )}
                        </div>
                      ))}
                  </div>
                ))}
              <div className="btn-container">
                <Link to="/" className="text-white">
                  <button className="btnNav">Previous</button>
                </Link>
                <button type="submit" className="btnNav">
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
