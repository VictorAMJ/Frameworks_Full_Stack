import Card from "../components/ProfileCard";

export default function ProfilePage() {
  return (
    <div>
        <h1>Profile Card</h1>
        <Card name="Gabriela" age={23} isStudent={true}/>
        <Card name="Victor" age={19} isStudent={true}/>
    </div>
  )
}