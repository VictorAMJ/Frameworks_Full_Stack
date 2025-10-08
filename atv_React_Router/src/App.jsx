//Esse arquivo é o coração das rotas

import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import Header from "./Components/Header" // Menu de navegação principal

//Paginas:
import HomePage from "./Pages/HomePage"
import IdPage from "./Pages/IdPage"
import NotFoundPage from "./Pages/NotFoundPage"
import ProfilePage from "./Pages/ProfilePage"

function App() {
    return (
        <Router>    {/*navegador*/}
            <Header/>   {/* cabeçalho (aparece em todas as paginas) */}
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/card" element={<ProfilePage />} />
                <Route path="/id/:id" element={<IdPage />} />
                <Route path="*" element={<NotFoundPage />} />  
            </Routes>
        </Router>
    )
}

export default App



