import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    login: null,
    name: null,
    surname: null,
    phone_number: null,
    email: null,
    description: null,
    dormitory: null,
    random_coffee_active: null,
    tags: null
};

const userSlice = createSlice({
  name: "user",
  initialState,
  reducers: {
    setUser(state, action){
      state.login = action.payload.login;
      state.name = action.payload.name;
      state.surname = action.payload.surname;
      state.phone_number = action.payload.phone_number;
      state.email = action.payload.email;
      state.description = action.payload.description;
      state.dormitory = action.payload.dormitory;
      state.random_coffee_active = action.payload.random_coffee_active;
      state.tags = action.payload.tags;
    },
  }
})

export const {setUser} = userSlice.actions;
export default userSlice.reducer;