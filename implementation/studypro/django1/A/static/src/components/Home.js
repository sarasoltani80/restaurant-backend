import { Fragment } from "react";
import MainNavigation from "./MainNavigation";
 
const Home = (props) => {
    return (
        <Fragment>
            <MainNavigation />
            <main>
                {props.children}
            </main>
        </Fragment>
    );
};

export default Home;