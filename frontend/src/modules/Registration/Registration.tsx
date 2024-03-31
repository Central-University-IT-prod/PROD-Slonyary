import React, {FC, useState} from "react";
import style from "./Registration.module.css";
import {Button, Grid, Link, TextField} from "@mui/material";
import {inputsProps} from "./inputsProps";
import {useActions} from "../../hooks/useActions";
import {useNavigate} from "react-router-dom";
import {NavigatePath, paths} from "../../routes";
import PageElement from "../../Ui/PageElement/PageElement";

export default function Registration(): FC {
  const [name, setName] = useState<string>("");
  const [dateBorn, setDateBorn] = useState<string>("");
  const {setUser} = useActions();
  const navigate = useNavigate();

  const onSubmit = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
    setUser({
      name,
      dateBorn: dateBorn || null,
    })
    navigate(NavigatePath(paths.HOME));
  };

  type changer = (e: React.ChangeEvent<HTMLInputElement>) => void;
  const nameOnChange: changer = (e) => setName(e.target.value);
  const dateOnChange: changer = (e) => setDateBorn(e.target.value);
  return (
    <div className={style.Registration_wrapper}>
      <div className="container">
        <PageElement>
          <h1 className={style.Registration_title}>Регистрация</h1>
          <Grid
            container
            spacing="15px"
            wrap="wrap"
            justifyContent="center"
          >
            <Grid item md={12} sm={12} xs={12}>
              <TextField
                {...inputsProps.name}
                value={name}
                onChange={nameOnChange}
              />
            </Grid>
            <Grid item md={6} sm={12} xs={12}>
              <TextField
                {...inputsProps.dateBorn}
                value={dateBorn}
                onChange={dateOnChange}
              />
            </Grid>
            <Grid item md={6} sm={12} xs={12}>
              <TextField
                {...inputsProps.email}
                value={dateBorn}
                onChange={dateOnChange}
              />
            </Grid>
          </Grid>
          <Button
            disabled={name.length === 0}
            variant="contained"
            sx={{m: "auto", display: "block", mt: 3}}
            onClick={onSubmit}
          >
            Зарегистрироваться
          </Button>
          <div className={style.Registration_loginBox}>
            <Link>У вас уже есть аккаунт? Войти</Link>
          </div>
        </PageElement>
      </div>
    </div>
  );
}
