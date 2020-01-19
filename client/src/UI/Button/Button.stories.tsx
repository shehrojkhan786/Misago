import { withKnobs, boolean } from "@storybook/addon-knobs"
import React from "react"
import { CardContainer, Gallery, RootContainer } from "../Storybook"
import Button, { ButtonType } from "."

export default {
  title: "UI/Button",
  decorators: [withKnobs],
}

const blockKnob = () => boolean("Block", false)
const disabledKnob = () => boolean("Disabled", false)
const loadingKnob = () => boolean("Loading", false)
const outlineKnob = () => boolean("Outline", false)

const types = [
  ButtonType.PRIMARY,
  ButtonType.SECONDARY,
  ButtonType.SUCCESS,
  ButtonType.WARNING,
  ButtonType.DANGER,
  ButtonType.LINK,
]

export const TextOnly = () => {
  const block = blockKnob()
  const disabled = disabledKnob()
  const loading = loadingKnob()
  const outline = outlineKnob()

  const items = types.map(type => ({
    name: type,
    component: (
      <Button
        block={block}
        text="Lorem ipsum"
        type={type}
        disabled={disabled}
        loading={loading}
        outline={outline}
      />
    ),
  }))

  return (
    <>
      <RootContainer>
        <Gallery items={items} />
      </RootContainer>
      <CardContainer>
        <Gallery items={items} />
      </CardContainer>
    </>
  )
}

export const IconOnly = () => {
  const block = blockKnob()
  const disabled = disabledKnob()
  const loading = loadingKnob()
  const outline = outlineKnob()

  const items = types.map(type => ({
    name: type,
    component: (
      <Button
        block={block}
        icon={"comment-alt"}
        type={type}
        disabled={disabled}
        loading={loading}
        outline={outline}
      />
    ),
  }))

  return (
    <>
      <RootContainer>
        <Gallery items={items} />
      </RootContainer>
      <CardContainer>
        <Gallery items={items} />
      </CardContainer>
    </>
  )
}

export const IconAndText = () => {
  const block = blockKnob()
  const disabled = disabledKnob()
  const loading = loadingKnob()
  const outline = outlineKnob()

  const items = types.map(type => ({
    name: type,
    component: (
      <Button
        block={block}
        icon={"comment-alt"}
        text="Start thread"
        type={type}
        disabled={disabled}
        loading={loading}
        outline={outline}
      />
    ),
  }))

  return (
    <>
      <RootContainer>
        <Gallery items={items} />
      </RootContainer>
      <CardContainer>
        <Gallery items={items} />
      </CardContainer>
    </>
  )
}