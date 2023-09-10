import { useState } from 'react';
import axios from 'axios';
import styles from './Login.module.css';
import { Link, useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { setUser } from '../../store/slices/userSlice';
export default function Login() {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [login, setLogin] = useState('');
  const [password, setPassword] = useState('');
  return (
    <div className={styles.main}>
      <form>
        <div className="space-y-12">
          <div className="border-b border-gray-900/10 pb-12">
            <h2 className="text-base font-semibold leading-7 text-gray-900">Вход в систему</h2>

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
                      value={login}
                      onChange={(e) => setLogin(e.target.value)}
                      id="login"
                      autoComplete="login"
                      className="pl-4 block flex-1 border-0 bg-transparent py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6 text-base"
                      placeholder="Логин"
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
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                      autoComplete="password"
                      className="pl-4 block flex-1 border-0 bg-transparent py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6 text-base"
                      placeholder="Пароль"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="mt-6 flex items-center justify-end gap-x-6">
          <Link to="/register">
            <button type="button" className="text-sm font-semibold leading-6 text-gray-900">
              Зарегестрироваться
            </button>
          </Link>
          <button
            type="submit"
            onClick={(e) => {
              e.preventDefault();
              axios
                .post('http://127.0.0.1:8000/database/get_user', {
                  login: login,
                  password: password,
                })
                .then((response) => {
                  if (response.status === 200) {
                    dispatch(setUser(response.data));
                    navigate('/');
                  }
                });
            }}
            className="rounded-md bg-sky-500 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-sky-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
            Вход
          </button>
        </div>
      </form>
    </div>
  );
}
