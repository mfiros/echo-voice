"use client"; // This is a client component 👈🏽

import { useState, useEffect } from "react";

// Compare this snippet from echo-voice\frontend\echo-voice\src\app\page.js:
function formatDate(epochTime) {
  const date = new Date(epochTime * 1000); // Multiply by 1000 to convert from seconds to milliseconds
  const day = date.getDate();
  const month = date.toLocaleString("default", { month: "short" });
  const year = date.getFullYear();
  const hour = date.getHours() % 12 || 12;
  const minute = String(date.getMinutes()).padStart(2, "0");
  const ampm = date.getHours() >= 12 ? "pm" : "am";

  return `${day}${getOrdinalSuffix(
    day
  )} ${month} ${year} ${hour}:${minute}${ampm}`;
}

function getOrdinalSuffix(day) {
  const suffixes = ["th", "st", "nd", "rd"];
  const relevantDigits = day % 100 > 10 && day % 100 < 20 ? 0 : day % 10;
  return suffixes[relevantDigits] || suffixes[0];
}

function Main() {
  // create state for vanity number
  const [vanityNumber, setVanityNumber] = useState(null);

  async function getVanityNumber() {
    try {
      const res = await fetch("api/fetchdata", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
          "x-api-key": process.env.NEXT_PUBLIC_API_KEY,
        },
      });

      const data = await res.json();
      return data;
    } catch (err) {
      console.log(err);
    }
  }

  useEffect(() => {
    getVanityNumber().then((data) => {
      setVanityNumber(data);
    });
  }, []);

  return (
    vanityNumber && (
      <main className="flex min-h-screen flex-col items-center justify-between p-20">
        <div className="z-10 w-full max-w-5xl items-center justify-evenly font-mono text-sm lg:flex">
          Welcome to Echo Voice, Your vanity number translator!. Dial the number{" "}
          {/* <code className="text-red-500"> +1 213-462-1468</code> */}
          <span class="bg-green-100 text-green-800 text-xs font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-green-900 dark:text-green-300">
            +1 213-462-1468
          </span>
          to get started.
        </div>

        <div className="relative flex place-items-center ">
          <div className="relative overflow-x-auto shadow-md sm:rounded-lg">
            <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
              <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                <tr>
                  <th scope="col" className="px-6 py-3">
                    Phone number
                  </th>
                  <th scope="col" className="px-6 py-3">
                    <div className="flex items-center">Vanity number</div>
                  </th>
                  <th scope="col" className="px-6 py-3">
                    <div className="flex items-center">Last called</div>
                  </th>
                </tr>
              </thead>
              {/* <tbody>
              <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                <th
                  scope="row"
                  className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                >
                  Apple MacBook Pro 17"
                </th>
                <td className="px-6 py-4">Silver</td>
                <td className="px-6 py-4">Laptop</td>
              </tr>
              <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                <th
                  scope="row"
                  className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                >
                  Microsoft Surface Pro
                </th>
                <td className="px-6 py-4">White</td>
                <td className="px-6 py-4">Laptop PC</td>
              </tr>
              <tr className="bg-white dark:bg-gray-800">
                <th
                  scope="row"
                  className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                >
                  Magic Mouse 2
                </th>
                <td className="px-6 py-4">Black</td>
                <td className="px-6 py-4">Accessories</td>
              </tr>
            </tbody> */}
              {vanityNumber &&
                vanityNumber.map((item) => (
                  <tbody>
                    <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                      <th
                        scope="row"
                        className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                        key={item.callerNumber}
                      >
                        <button
                          type="button"
                          key={item.callerNumber}
                          className="text-white bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2"
                        >
                          {item.callerNumber}
                        </button>
                      </th>
                      <td className="px-6 py-4">
                        {item.result.map((i) => (
                          //   <span className="bg-blue-100 text-blue-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-blue-900 dark:text-blue-300">
                          //     {item}
                          //   </span>
                          <button
                            type="button"
                            key={i}
                            className="text-white uppercase bg-gradient-to-br from-purple-600 to-blue-500 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 "
                          >
                            {i}
                          </button>
                        ))}
                      </td>

                      <td className="px-6 py-4" key={item.lastcalled}>
                        <span className="bg-blue-100 text-blue-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-blue-900 dark:text-blue-300">
                          {formatDate(item.lastcalled)}
                        </span>
                      </td>
                    </tr>
                  </tbody>
                ))}
            </table>
          </div>
        </div>

        <footer class=" rounded-lg shadow m-4 dark:bg-gray-800">
          <div class="w-full mx-auto max-w-screen-xl p-4 md:flex md:items-center md:justify-between">
            {/* <span class="text-sm text-gray-500 sm:text-center dark:text-gray-400">
              © 2023{" "}
              <a href="https://flowbite.com/" class="hover:underline">
                Firos M
              </a>
              . All Rights Reserved.
            </span> */}
            <ul class="flex flex-wrap items-center mt-3 text-sm font-medium text-gray-500 dark:text-gray-400 sm:mt-0 ml-10">
              {/* <li>
                <a href="#" class="mr-4 hover:underline md:mr-6 ">
                  About
                </a>
              </li> */}
              <li>
                <a href="#" class="mr-4 hover:underline md:mr-6">
                  Privacy Policy
                </a>
              </li>
              <li>
                <a href="#" class="mr-4 hover:underline md:mr-6">
                  Licensing
                </a>
              </li>
              <li>
                <a href="#" class="hover:underline">
                  Contact
                </a>
              </li>
            </ul>
          </div>
        </footer>
      </main>
    )
  );
}

export default Main;
