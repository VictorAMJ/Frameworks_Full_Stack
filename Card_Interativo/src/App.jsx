import React from "react";
import Card from "./ProfileCard";

function App() {
    return (
        <div>
            <Card name="Victor" age={19} isStudent={true} />
            <Card name="Robert Oppenheimer" age={62} isStudent={false} />
        </div>
    )
}

export default App