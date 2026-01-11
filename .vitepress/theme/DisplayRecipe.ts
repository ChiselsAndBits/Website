type OnlyFirstChar<S extends string> = S extends `${infer $TFirstChar}${string}`
  ? $TFirstChar
  : string;

type OnlyTwoChar<S extends string> = S extends `${infer $TFirstChar}${infer $SecondChar}${string}`
  ? $TFirstChar
  : string;

type OnlyThreeChar<S extends string> = S extends `${infer $TFirstChar}${infer $SecondChar}${infer $ThirdChar}${string}`
  ? $TFirstChar
  : string;

type SingleChar = string extends string & OnlyFirstChar<string>
  ? string & OnlyFirstChar<string>
  : string & { length: 1 };

type TwoCharacterRecipeLine = string extends string & OnlyTwoChar<string>
  ? string & OnlyTwoChar<string>
  : string & { length: 2};

type ThreeCharacterRecipeLine = string extends string & OnlyThreeChar<string>
  ? string & OnlyThreeChar<string>
  : string & { length: 3};

export type ThreeByThreeRecipeContents = readonly [ ThreeCharacterRecipeLine, ThreeCharacterRecipeLine, ThreeCharacterRecipeLine ]
export type TwoByTwoRecipeContents = readonly [ TwoCharacterRecipeLine, TwoCharacterRecipeLine ]
export type RecipeContents = (ThreeByThreeRecipeContents | TwoByTwoRecipeContents)

export interface ItemIngredient {
  namespace: string,
  location: string,
  title: string,
  isTag: false
}

export interface TagIngredient {
  namespace: string,
  location: string,
  isTag: true
}

export type Ingredient = (ItemIngredient | TagIngredient)

export interface DisplayRecipe {
  ingredients: Map<SingleChar, Ingredient>
  contents: RecipeContents
}

export interface ShapelessRecipe extends DisplayRecipe {
  isShapeless: true
}

export interface ShapedRecipe extends DisplayRecipe {
  isShapeless: false
}

export type Recipe = (ShapedRecipe | ShapelessRecipe)

export function IsTagIngredient(ingredient : Ingredient) : boolean {
  return "isTag" in ingredient && ingredient.isTag
}