import { useEffect, useState } from 'react';
import styles from './Registration.module.css';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import { useDispatch } from 'react-redux';
import { setUser } from '../../store/slices/userSlice';

export default function Registration() {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [login, setLogin] = useState('');
  const [password, setPassword] = useState('');
  const [about, setAbout] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [dormitory, setDormitory] = useState('Металлург-1');
  const [coffee, setCoffee] = useState(false);
  const [phoneNumber, setPhoneNumber] = useState('');
  const [tags, setTags] = useState([]);
  const [search, setSearch] = useState('');
  const [customTag, setCustomTag] = useState('');
  const [finalTags, setFinalTags] = useState([]);
  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/database/get_all_tags')
      .then((response) => setTags(response.data));
  }, []);
  return (
    <div className={styles.main}>
      <form>
        <div className="space-y-12">
          <div className="border-b border-gray-900/10 pb-12">
            <h2 className="text-base font-semibold leading-7 text-gray-900">Регистрация</h2>
            <p className="mt-1 text-sm leading-6 text-gray-600">
              Эта информация будет опубликована в открытом доступе, поэтому будьте внимательны к
              тому, чем вы делитесь.
            </p>

            <div className="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
              <div className="sm:col-span-4">
                <label
                  htmlFor="login"
                  className="block text-sm font-medium leading-6 text-gray-900">
                  Логин
                </label>
                <div className="mt-2">
                  <div className="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md">
                    <input
                      type="text"
                      name="login"
                      id="login"
                      autoComplete="login"
                      className="pl-4 block flex-1 border-0 bg-transparent py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6 text-base"
                      placeholder="Логин"
                      value={login}
                      onChange={(e) => setLogin(e.target.value)}
                    />
                  </div>
                </div>
              </div>

              <div className="sm:col-span-4">
                <label
                  htmlFor="password"
                  className="block text-sm font-medium leading-6 text-gray-900">
                  Пароль
                </label>
                <div className="mt-2">
                  <div className="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md">
                    <input
                      type="password"
                      name="password"
                      id="password"
                      autoComplete="password"
                      className="pl-4 block flex-1 border-0 bg-transparent py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6 text-base"
                      placeholder="Пароль"
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                    />
                  </div>
                </div>
              </div>

              <div className="col-span-full">
                <label
                  htmlFor="about"
                  className="block text-sm font-medium leading-6 text-gray-900">
                  О себе
                </label>
                <div className="mt-2">
                  <textarea
                    id="about"
                    name="about"
                    rows={3}
                    className="block w-full rounded-md border-0 py-1.5 px-4 text-sm text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                    value={about}
                    onChange={(e) => {
                      setAbout(e.target.value);
                      console.log(e.target.value);
                    }}
                  />
                </div>
                <p className="mt-3 text-sm leading-6 text-gray-600">
                  Напишите несколько предложений о себе.
                </p>
              </div>
            </div>
          </div>

          <div className="border-b border-gray-900/10 pb-12">
            <h2 className="text-base font-semibold leading-7 text-gray-900">
              Персональная информация
            </h2>

            <div className="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
              <div className="sm:col-span-3">
                <label
                  htmlFor="first-name"
                  className="block text-sm font-medium leading-6 text-gray-900">
                  Имя
                </label>
                <div className="mt-2">
                  <input
                    type="text"
                    name="first-name"
                    id="first-name"
                    autoComplete="given-name"
                    placeholder="Имя"
                    value={firstName}
                    onChange={(e) => setFirstName(e.target.value)}
                    className="block w-full rounded-md border-0 px-4 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>

              <div className="sm:col-span-3">
                <label
                  htmlFor="last-name"
                  className="block text-sm font-medium leading-6 text-gray-900">
                  Фамилия
                </label>
                <div className="mt-2">
                  <input
                    type="text"
                    name="last-name"
                    id="last-name"
                    placeholder="Фамилия"
                    value={lastName}
                    onChange={(e) => setLastName(e.target.value)}
                    autoComplete="family-name"
                    className="block w-full rounded-md border-0 py-1.5 px-4 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>

              <div className="sm:col-span-4">
                <label
                  htmlFor="password"
                  className="block text-sm font-medium leading-6 text-gray-900">
                  Номер телефона
                </label>
                <div className="mt-2">
                  <div className="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md">
                    <input
                      type="text"
                      name="phone"
                      id="phone"
                      autoComplete="phone-number"
                      className="pl-4 block flex-1 border-0 bg-transparent py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6 text-base"
                      placeholder="Номер телефона"
                      value={phoneNumber}
                      onChange={(e) => setPhoneNumber(e.target.value)}
                    />
                  </div>
                </div>
              </div>

              <div className="sm:col-span-4">
                <label
                  htmlFor="email"
                  className="block text-sm font-medium leading-6 text-gray-900">
                  Email адрес
                </label>
                <div className="mt-2">
                  <input
                    id="email"
                    name="email"
                    type="email"
                    placeholder="Email"
                    autoComplete="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className="block w-full rounded-md border-0 py-1.5 px-4 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>

              <div className="sm:col-span-3">
                <label
                  htmlFor="dormitory"
                  className="block text-sm font-medium leading-6 text-gray-900">
                  Общежитие
                </label>
                <div className="mt-2">
                  <select
                    id="cdormitory"
                    name="dormitory"
                    autoComplete="dormitory-name"
                    value={dormitory}
                    onChange={(e) => setDormitory(e.target.value)}
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6">
                    <option>Металлург-1</option>
                    <option>Металлург-2</option>
                    <option>Металлург-3</option>
                    <option>Металлург-4</option>
                    <option>Горняк 1</option>
                    <option>Горняк 2</option>
                    <option>Дом-коммуна</option>
                    <option>ДСГ-5</option>
                    <option>ДСГ-6</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
          <fieldset>
            <legend className="text-base font-semibold leading-6 text-gray-900">Интересы</legend>
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
            <div className="flex flex-wrap mt-6 gap-x-10 min-h-[120px]">
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
          <div className="mt-10 space-y-10">
            <fieldset>
              <legend className="text-base font-semibold leading-6 text-gray-900">
                Random Coffee
              </legend>
              <p className="mt-1 text-sm leading-6 text-gray-600">
                Сервис Random Coffee предоставит вам возможность случайных встреч с другими
                студентами посредством Telegram бота.
              </p>
              <div className="mt-6 space-y-6">
                <div className="flex items-center gap-x-3">
                  <input
                    id="push-everything"
                    name="push-notifications"
                    type="radio"
                    value={coffee}
                    onChange={(e) => {
                      setCoffee(e.target.id === 'push-everything' ? true : false);
                    }}
                    className="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"
                  />
                  <label
                    htmlFor="push-everything"
                    className="block text-sm font-medium leading-6 text-gray-900">
                    Использовать
                  </label>
                </div>
                <div className="flex items-center gap-x-3">
                  <input
                    id="push-nothing"
                    name="push-notifications"
                    type="radio"
                    value={coffee}
                    onChange={(e) => {
                      setCoffee(e.target.id === 'push-everything' ? true : false);
                    }}
                    className="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"
                  />
                  <label
                    htmlFor="push-nothing"
                    className="block text-sm font-medium leading-6 text-gray-900">
                    Не использовать
                  </label>
                </div>
              </div>
            </fieldset>
          </div>
        </div>

        <div className="mt-6 flex items-center justify-end gap-x-6">
          <Link to="/login">
            <button type="button" className="text-sm font-semibold leading-6 text-gray-900">
              Уже есть аккаунт
            </button>
          </Link>
          <button
            onClick={(e) => {
              e.preventDefault();
              axios
                .post('http://127.0.0.1:8000/database/create_user', {
                  login: login,
                  name: firstName,
                  surname: lastName,
                  phone_number: phoneNumber,
                  email: email,
                  description: about,
                  dormitory: dormitory,
                  random_coffee_active: coffee,
                  password: password,
                  tags: [...finalTags],
                })
                .then((response) => {
                  if (response.status === 200) {
                    dispatch(setUser(response.data));
                    navigate('/');
                  }
                });
            }}
            className="rounded-md bg-sky-500 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-sky-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
            Зарегестрироваться
          </button>
        </div>
      </form>
    </div>
  );
}
