import classes from './MainNavigation.module.css';
import "../../node_modules/bootstrap/dist/css/bootstrap.css";
// import { NavLink } from 'react-router-dom';

const MainNavigation = () => {
    return (
        <nav className="navbar navbar-expand-lg bg-body-tertiary">
            <div className="container-fluid">
                <a className="navbar-brand" href=""> 
                    <span className={classes['logo_first']}>Book</span>
                    <span className={classes['logo_second']}>Club</span>
                </a>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                        <li className="nav-item">
                        <a className="nav-link active" aria-current="page" href="#">
                            Home
                        </a>
                        </li>
                        <li className="nav-item">
                        <a className="nav-link" href="#">
                            Books
                        </a>
                        </li>
                        <li className="nav-item">
                        <a className="nav-link" href="#">
                            Browse
                        </a>
                        </li>
                        <li className="nav-item">
                        <a className="nav-link" href="#">
                            Community
                        </a>
                        </li>
                    </ul>
                    <ul className="navbar-nav ms-auto mb-2 mb-lg-0">
                        <li className="nav-item">
                        <a className="nav-link" href="#">
                            Sign in
                        </a>
                        </li>
                        <li className="nav-item">
                        <a className="nav-link" href="#">
                            Sing up
                        </a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    );
};

export default MainNavigation;