import styles from './Header.module.css';
import logo from '../../assets/misishub2.png';
export default function Header() {
  return (
    <>
      <header className={styles.main}>
        <div>
          <img className="inline-block h-[80px] mt-1" src={logo} alt="" />
        </div>
        <div className={styles.links}>
          <a className={styles.link} href="#">
            Клубы
          </a>
          <a className={styles.link} href="#">
            События
          </a>
          <a className={styles.link} href="#">
            Анкеты
          </a>
          <a className={styles.link} href="#">
            Профиль
          </a>
        </div>
      </header>
      <div className={styles.line}></div>
    </>
  );
}
