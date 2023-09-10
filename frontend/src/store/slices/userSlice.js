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
    tags: null,
    telegram: null,
    clubs: null,
    events: null,
    last_random_coffee_meet: null,
    id: null,
    form_responders: null
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
      action.payload.telegram ? state.telegram = action.payload.telegram : null
      action.payload.clubs ? state.clubs = action.payload.clubs : null
      action.payload.events ? state.events = action.payload.events : null
      action.payload.last_random_coffee_meet ? state.last_random_coffee_meet = action.payload.last_random_coffee_meet : null
      action.payload.id ? state.id = action.payload.id : null
      action.payload.form_responders ? state.form_responders = action.payload.form_responders : null
    },
  }
})

export const {setUser} = userSlice.actions;
export default userSlice.reducer;