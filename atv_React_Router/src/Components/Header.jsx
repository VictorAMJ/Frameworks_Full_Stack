import { Link } from "react-router-dom" //importação pra criar navegação interna

function Header() {
    return (
        <header>
            <Link to="/">Home</Link> |{" "} {/*separador de links*/}
            <Link to="/card">Perfil</Link>
            <Link to="/id"></Link>
        </header>
    )
}








