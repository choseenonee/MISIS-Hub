import axios from 'axios';
import React, { useEffect, useState } from 'react';

export default function Forms() {
  let [data, setData] = useState([]);
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/database/get_all_forms').then((response) => {
      setData(response.data);
    });
  }, []);
  return (
    <>
      {data.map((elem, idx) => {
        return (
          <div key={idx} className="pl-[380px] pr-[380px]">
            <div className="border-solid border-2 border-gray-400 rounded-xl p-3 mt-10">
              <div className="px-4 sm:px-0">
                <h3 className="text-base font-semibold leading-7 text-gray-900">Анкета</h3>
                <p className="mt-1 max-w-2xl text-sm leading-6 text-gray-500">{elem.form_type}</p>
              </div>
              <div className="mt-3 border-t border-gray-100">
                <dl className="divide-y divide-gray-100">
                  <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                    <dt className="text-sm font-medium leading-6 text-gray-900">Имя и фамилия</dt>
                    <dd className="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                      {elem.author.name + ' ' + elem.author.surname}
                    </dd>
                  </div>

                  <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                    <dt className="text-sm font-medium leading-6 text-gray-900">О себе</dt>
                    <dd className="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                      {elem.author.description}
                    </dd>
                  </div>

                  <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                    <dt className="text-sm font-medium leading-6 text-gray-900">Теги</dt>
                    <dd className="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                      {elem.author.tags.map((tag) => tag + ' ')}
                    </dd>
                  </div>

                  <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                    <dt className="text-sm font-medium leading-6 text-gray-900">Описание анкеты</dt>
                    <dd className="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                      {elem.description}
                    </dd>
                  </div>

                  <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                    <dt className="text-sm font-medium leading-6 text-gray-900">Теги анкеты</dt>
                    <dd className="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                      {elem.tags.map((tag) => tag + ' ')}
                    </dd>
                  </div>
                </dl>
              </div>
            </div>
          </div>
        );
      })}
    </>
  );
}
