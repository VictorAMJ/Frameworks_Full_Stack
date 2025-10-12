import { Link } from "react-router-dom";

export default function Header() {
  return (
    <header>
      <nav>
        <ul>
          <Link to="/">Buscador de CEP</Link>|{" "}
          <Link to="/profile">Profile</Link>|{" "}
          <Link to="/saiba_mais">Saiba mais</Link>
        </ul>
      </nav>
    </header>
  );
}