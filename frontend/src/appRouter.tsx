import { createBrowserRouter } from "react-router-dom";
import RegistrationPage from "./pages/RegistrationPage";
import App from "./App";
import { paths } from "./routes";
import HomePage from "./pages/HomePage";

export const router = createBrowserRouter([
	{
		element: <App />,
		path: "/",
		children: [
			{
				path: paths.REGISTRATION,
				element: <RegistrationPage />,
			},
			{
				path: paths.HOME,
				element: <HomePage />,
			},
		],
	},
]);
