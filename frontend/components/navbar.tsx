// file for code for mui navbar component

import * as React from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import CssBaseline from "@mui/material/CssBaseline";
import useScrollTrigger from "@mui/material/useScrollTrigger";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import { makeStyles } from "@material-ui/core/styles";
import MenuIcon from "@material-ui/icons/Menu";
import IconButton from "@material-ui/core/IconButton";
import Button from "@material-ui/core/Button";

const useStyles = makeStyles((theme) => ({
	root: {
		flexGrow: 1,
	},
	menuButton: {
		marginRight: theme.spacing(2),
	},
	title: {
		flexGrow: 1,
	},

	button: {
		margin: theme.spacing(1),
		color: "white",
		backgroundColor: "#3f51b5",
		border: "none",
		borderRadius: "5px",
		right: "0",
	},
}));

interface Props {
	/**
	 * Injected by the documentation to work in an iframe.
	 * You won't need it on your project.
	 */
	window?: () => Window;
	children: React.ReactElement;
}

function ElevationScroll(props: Props) {
	const { children, window } = props;
	// Note that you normally won't need to set the window ref as useScrollTrigger
	// will default to window.
	// This is only being set here because the demo is in an iframe.
	const trigger = useScrollTrigger({
		disableHysteresis: true,
		threshold: 0,
		target: window ? window() : undefined,
	});

	return React.cloneElement(children, {
		elevation: trigger ? 4 : 0,
	});
}

export default function Navbar(props: Props) {
	const classes = useStyles();
	// make css class for button

	return (
        
		<React.Fragment>
			<CssBaseline />
			<ElevationScroll {...props}>
            <div className={classes.root}>
				<AppBar position="fixed" style={{backgroundColor:"" }}>
					<Toolbar>
						<IconButton
							edge="start"
							className={classes.menuButton}
							color="inherit"
							aria-label="menu"
						>
							<MenuIcon />
						</IconButton>
						<Typography variant="h6" className={classes.title}>
							NBDT
						</Typography>
						<Button color="inherit">Login</Button>
						<Button color="inherit">Sign Up</Button>
						{/* route to broweser reviewer */}
					</Toolbar>
				</AppBar>
                </div>
			</ElevationScroll>
			<Toolbar />
		</React.Fragment>
        
	);
}

// Language: typescript
// Path: muxt-ts/pages/index.tsx
// Compare this snippet from muxt-ts/pages/index.tsx:
