// new page for search abstract
import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import IconButton, { IconButtonProps } from "@mui/material/IconButton";
import MenuIcon from "@material-ui/icons/Menu";
import { styled } from "@mui/material/styles";
import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Card from "@mui/material/Card";
import CardHeader from "@mui/material/CardHeader";
import CardMedia from "@mui/material/CardMedia";
import CardContent from "@mui/material/CardContent";
import CardActions from "@mui/material/CardActions";
import Collapse from "@mui/material/Collapse";
import Avatar from "@mui/material/Avatar";
import { red } from "@mui/material/colors";
import FavoriteIcon from "@mui/icons-material/Favorite";
import ShareIcon from "@mui/icons-material/Share";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import MoreVertIcon from "@mui/icons-material/MoreVert";
import CircularProgress, {
	circularProgressClasses,
	CircularProgressProps,
} from "@mui/material/CircularProgress";
import LinearProgress, {
	linearProgressClasses,
} from "@mui/material/LinearProgress";
import InfoIcon from "@mui/icons-material/Info";
import MailIcon from "@mui/icons-material/Mail";
import SchoolIcon from "@mui/icons-material/School";

import Navbar from "../components/navbar";
import data from "./data.json";

const BorderLinearProgress = styled(LinearProgress)(({ theme }) => ({
	height: 10,
	borderRadius: 5,
	[`&.${linearProgressClasses.colorPrimary}`]: {
		backgroundColor:
			theme.palette.grey[theme.palette.mode === "light" ? 200 : 800],
	},
	[`& .${linearProgressClasses.bar}`]: {
		borderRadius: 5,
		backgroundColor: theme.palette.mode === "light" ? "#1a90ff" : "#308fe8",
	},
}));

interface ExpandMoreProps extends IconButtonProps {
	expand: boolean;
}

const ExpandMore = styled((props: ExpandMoreProps) => {
	const { expand, ...other } = props;
	return <IconButton {...other} />;
})(({ theme, expand }) => ({
	transform: !expand ? "rotate(0deg)" : "rotate(180deg)",
	marginLeft: "auto",
	transition: theme.transitions.create("transform", {
		duration: theme.transitions.duration.shortest,
	}),
}));

function getResults({searchText}) {
    // alert(searchText);
}

function RecipeReviewCard({ data }) {
	const [expanded, setExpanded] = React.useState(false);

	const handleExpandClick = () => {
		setExpanded(!expanded);
	};

	return (
		<Card sx={{ minWidth: "80%" }}>
			<CardHeader
				action={
					<Button
						variant="contained"
						color="primary"
						endIcon={<InfoIcon />}
						href={data.infoLink}
						target="_blank"
					>
						Info
					</Button>
				}
				title={data.name}
				subheader={data.affiliation}
			/>

			<CardContent>
				<BorderLinearProgress
					variant="determinate"
					value={data.value}
					style={{ width: "30%" }}
				/>
				<Typography variant="body2" color="text.secondary">
					{data.content}
				</Typography>
			</CardContent>
			<CardActions style={{}}>
				<IconButton aria-label="mail">
					<MailIcon
						onClick={() => window.open(data.mailLink, "_blank")}
					/>
				</IconButton>
				<IconButton aria-label="scholar">
					<SchoolIcon
						onClick={() => window.open(data.scholarLink, "_blank")}
					/>
				</IconButton>
			</CardActions>
		</Card>
	);
}

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
}));

export default function SearchAbstract() {
	// page with a text field with helper text "enter abstract", and a submit button to submit

	const AbstractButton: React.FC = () => {
		// set style for the Button

		const Button = styled("button")(({ theme }) => ({
			// button at thr centre
			position: "absolute",
			top: "50%",
			left: "50%",
			transform: "translate(-50%, -50%)",
			// button size
			// button color

			backgroundColor: "#3f51b5",
			color: "white",
			// button border
			border: "none",
			borderRadius: "5px",
			// button font
		}));
		return <Button>Submit</Button>;
	};

	const [searchText, setSearchText] = React.useState("");
	const prompt =
		"Enter the abstract of the paper for which you want to search reviewers.";
	const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
		setSearchText(event.target.value);
	};
	const [reviewersData, setReviewersData] = React.useState([]);

	return (
		<>
			<Box sx={{ flexGrow: 3 }}>
				<Grid container spacing={2}>
					<Grid container item spacing={1}>
						<Box sx={{ flexGrow: 1 }}>
							<Navbar />
						</Box>
					</Grid>
					<Grid
						container
						item
						spacing={1}
						style={{
							display: "flex",
							justifyContent: "center",
							alignItems: "center",
							width: "100%",
						}}
					>
						<TextField
							id="filled-multiline-flexible"
							placeholder={prompt}
							multiline
							minRows={15}
							maxRows={15}
							value={searchText}
							onChange={handleChange}
							variant="filled"
							sx={{ m: 1, width: "80%" }}
						/>
					</Grid>
					<Grid
						container
						style={{
							display: "flex",
							justifyContent: "right",
							alignItems: "right",
							marginRight: "11%",
						}}
					>
						<Button
							variant="contained"
							color="primary"
							onClick={() => {
                                getResults({searchText});
                                setReviewersData(data);
							}}
						>
							{" "}
							Get Reviewers
						</Button>
					</Grid>

					<Grid
						container
						spacing={1}
						style={{
							display: "flex",
							justifyContent: "center",
							alignItems: "center",
							minHeight: "10vh",
						}}
					></Grid>
					<Grid
						container
						item
						spacing={1}
						style={{
							display: "flex",
							justifyContent: "center",
							alignItems: "center",
							width: "100%",
						}}
					>
						{
							// call a function to get the data from json data
							reviewersData.map((item) => (
								<Grid
									container
									item
									spacing={1}
									style={{
										display: "flex",
										justifyContent: "center",
										alignItems: "center",
										width: "100%",
										marginBottom: "2%",
									}}
								>
									<RecipeReviewCard data={item} />
								</Grid>
							))
						}
					</Grid>
				</Grid>
			</Box>
		</>
	);
}
