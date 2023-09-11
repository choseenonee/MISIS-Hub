import React, { useEffect, useState } from 'react';
import styles from './HomePage.module.css';
import { useSelector } from 'react-redux';
import axios from 'axios';

export default function HomePage() {
  const [tags, setTags] = useState([]);
  const [search, setSearch] = useState('');
  const [customTag, setCustomTag] = useState('');
  const [finalTags, setFinalTags] = useState([]);
  const [about, setAbout] = useState('');
  const [type, setType] = useState('поиск studdy-buddy');
  const data = useSelector((state) => state.user);
  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/database/get_all_tags')
      .then((response) => setTags(response.data));
  }, []);

  return (
    <>
      <div className={styles.main}>
        <div>
          <div className="px-4 sm:px-0">
            <h3 className="text-base font-semibold leading-7 text-gray-900">Личный кабинет</h3>
            <p className="mt-1 max-w-2xl text-sm leading-6 text-gray-500">
              Информация о пользователе.
            </p>
          </div>
          <div className="mt-6 border-t border-gray-100">
            <dl className="divide-y divide-gray-100">
              <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                <dt className="text-sm font-medium leading-6 text-gray-900">Имя и фамилия</dt>
                <dd className="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                  {data.name + ' ' + data.surname}
                </dd>
              </div>
              <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                <dt className="text-sm font-medium leading-6 text-gray-900">Номер телефона</dt>
                <dd className="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                  {data.phone_number}
                </dd>
              </div>
              <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                <dt className="text-sm font-medium leading-6 text-gray-900">Email адрес</dt>
                <dd className="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                  {data.email}
                </dd>
              </div>
              <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                <dt className="text-sm font-medium leading-6 text-gray-900">О себе</dt>
                <dd className="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                  {data.description}
                </dd>
              </div>
              <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                <dt className="text-sm font-medium leading-6 text-gray-900">Общежитие</dt>
                <dd className="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                  {data.dormitory}
                </dd>
              </div>
              <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                <dt className="text-sm font-medium leading-6 text-gray-900">Теги</dt>
                <dd className="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                  {data.tags.map((elem) => elem + ' ')}
                </dd>
              </div>
            </dl>
          </div>
        </div>
      </div>

      <div className={styles.main}>
        <form>
          <div className="space-y-12">
            <div className="border-b border-gray-900/10 pb-12">
              <h2 className="text-base font-semibold leading-7 text-gray-900">Создание анкеты</h2>

              <div className="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
                <div className="col-span-full">
                  <label
                    htmlFor="about"
                    className="block text-sm font-medium leading-6 text-gray-900">
                    Описание заявки
                  </label>
                  <div className="mt-2">
                    <textarea
                      id="about"
                      name="about"
                      rows={3}
                      className="block w-full rounded-md border-0 py-1.5 px-4 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                      value={about}
                      onChange={(e) => setAbout(e.target.value)}
                    />
                  </div>
                </div>

                <div className="sm:col-span-3">
                  <label
                    htmlFor="country"
                    className="block text-sm font-medium leading-6 text-gray-900">
                    Тип заявки
                  </label>
                  <div className="mt-2">
                    <select
                      id="country"
                      name="country"
                      autoComplete="country-name"
                      value={type}
                      onChange={(e) => setType(e.target.value)}
                      className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6">
                      <option>поиск studdy-buddy</option>
                      <option>поиск напарников для проекта</option>
                      <option>поиск сожителя в общежитие</option>
                    </select>
                  </div>
                </div>
              </div>
              <fieldset className="mt-[65px]">
                <legend className="text-base font-semibold leading-6 text-gray-900">Теги</legend>
                <div className="mt-2 relative">
                  <input
                    type="text"
                    name="search"
                    id="search"
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                    placeholder="Поиск"
                    autoComplete="family-name"
                    className="block w-80 rounded-md border-0 py-1.5 pl-9 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                  <div className="w-6 h-6 absolute left-1.5 top-1.5">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      x="0px"
                      y="0px"
                      width="100"
                      height="100"
                      viewBox="0 0 24 24"
                      fill="#EBEBEB">
                      <path d="M 9 2 C 5.1458514 2 2 5.1458514 2 9 C 2 12.854149 5.1458514 16 9 16 C 10.747998 16 12.345009 15.348024 13.574219 14.28125 L 14 14.707031 L 14 16 L 20 22 L 22 20 L 16 14 L 14.707031 14 L 14.28125 13.574219 C 15.348024 12.345009 16 10.747998 16 9 C 16 5.1458514 12.854149 2 9 2 z M 9 4 C 11.773268 4 14 6.2267316 14 9 C 14 11.773268 11.773268 14 9 14 C 6.2267316 14 4 11.773268 4 9 C 4 6.2267316 6.2267316 4 9 4 z"></path>
                    </svg>
                  </div>
                </div>
                <div className="flex flex-wrap mt-6 gap-x-10 min-h-[120px] h-fit">
                  {search
                    ? tags
                        .filter((elem) => elem.tag.toLowerCase().includes(search.toLowerCase()))
                        .map((elem, idx) => {
                          return (
                            <div key={idx} className="relative flex gap-x-2">
                              <div className="flex h-6 items-center">
                                <input
                                  id={elem.tag}
                                  name={elem.tag}
                                  onChange={(e) =>
                                    setFinalTags([...finalTags, e.target.checked && e.target.name])
                                  }
                                  type="checkbox"
                                  className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600"
                                />
                              </div>
                              <div className="text-sm leading-6">
                                <label htmlFor={elem.tag} className="font-medium text-gray-900">
                                  {elem.tag}
                                </label>
                              </div>
                            </div>
                          );
                        })
                    : tags.map((elem, idx) => {
                        return (
                          <div key={idx} className="relative flex gap-x-2">
                            <div className="flex h-6 items-center">
                              <input
                                id={elem.tag}
                                name={elem.tag}
                                type="checkbox"
                                onChange={(e) =>
                                  e.target.checked
                                    ? setFinalTags([...finalTags, e.target.name])
                                    : setFinalTags([
                                        ...finalTags.filter((elem) => elem !== e.target.name),
                                      ])
                                }
                                className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600"
                              />
                            </div>
                            <div className="text-sm leading-6">
                              <label htmlFor={elem.tag} className="font-medium text-gray-900">
                                {elem.tag}
                              </label>
                            </div>
                          </div>
                        );
                      })}
                </div>
                <legend className="text-sm font-semibold mt-4 mb-3 leading-6 text-gray-900">
                  Добавление своего тега
                </legend>
                <div className="flex gap-x-5">
                  <input
                    type="text"
                    name="customtag"
                    id="customtag"
                    placeholder="Тег"
                    value={customTag}
                    onChange={(e) => setCustomTag(e.target.value)}
                    autoComplete="family-name"
                    className="block w-80 rounded-md border-0 py-1.5 px-4 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                  <button
                    onClick={(e) => {
                      e.preventDefault();
                      axios
                        .post('http://127.0.0.1:8000/create_tag', {
                          tag: customTag,
                        })
                        .then((response) => {
                          response.status === 200 && setTags([...tags, { tag: customTag }]);
                        });
                    }}
                    className="rounded-md bg-sky-500 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-sky-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
                    Создать тег
                  </button>
                </div>
              </fieldset>
            </div>
          </div>

          <div className="mt-6 flex items-center justify-end gap-x-6">
            <button
              type="submit"
              onClick={(e) => {
                e.preventDefault();
                console.log({
                  author_login: data.login,
                  description: about,
                  form_type: type,
                  tags: finalTags,
                });
                axios.post('http://127.0.0.1:8000/database/create_form', {
                  author_login: data.login,
                  description: about,
                  form_type: type,
                  tags: finalTags,
                });
              }}
              className="w-[120px] rounded-md bg-sky-500 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-sky-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
              Создать
            </button>
          </div>
        </form>
      </div>
    </>
  );
}
